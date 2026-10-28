"""Regressioni reali dell'hook: python -m unittest discover -s strumenti -p test_controlla.py."""
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1]


class HookNoteTest(unittest.TestCase):
    def git(self, cwd, *args):
        return subprocess.run(["git", "-C", str(cwd), *args], env=self.env,
                              capture_output=True, text=True, encoding="utf-8", errors="replace")

    def prepara(self, parent, linked):
        root = parent / "repo"
        root.mkdir()
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        self.env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_AUTHOR_NAME="Fixture", GIT_AUTHOR_EMAIL="fixture@example.invalid",
                        GIT_COMMITTER_NAME="Fixture", GIT_COMMITTER_EMAIL="fixture@example.invalid")
        self.assertEqual(self.git(root, "init").returncode, 0)
        notes = root / "raw" / "sessioni"
        notes.mkdir(parents=True)
        (notes / "2020-01-01-storica.md").write_text("# Nota storica\n", encoding="utf-8")
        (root / "strumenti").mkdir()
        shutil.copy2(SOURCE / "strumenti" / "controlla.py", root / "strumenti" / "controlla.py")
        hook = (SOURCE / ".githooks" / "pre-commit").read_text(encoding="utf-8")
        # Stessa guardia raw, stesso controllo Python; solo i controlli wiki estranei sono esclusi dalla fixture.
        hook = hook.replace("exec sh strumenti/controlli.sh",
                            f"exec {shlex.quote(Path(sys.executable).as_posix())} strumenti/controlla.py .")
        (root / ".githooks").mkdir()
        (root / ".githooks" / "pre-commit").write_text(hook, encoding="utf-8", newline="\n")
        (root / ".githooks" / "pre-commit").chmod(0o755)
        self.assertEqual(self.git(root, "add", ".").returncode, 0)
        self.assertEqual(self.git(root, "commit", "-m", "base fixture").returncode, 0)
        self.assertEqual(self.git(root, "config", "core.hooksPath", ".githooks").returncode, 0)
        if linked:
            wt = parent / "linked"
            result = self.git(root, "worktree", "add", "-b", "prova", str(wt))
            self.assertEqual(result.returncode, 0, result.stderr)
            return wt
        return root

    def test_nota_valida_con_storica_senza_campi_nuovi(self):
        for linked in (False, True):
            with self.subTest(linked=linked), tempfile.TemporaryDirectory() as tmp:
                root = self.prepara(Path(tmp), linked)
                new = "raw/sessioni/2020-01-02-valida.md"
                (root / new).write_text("# Nuova\n- **Costo:** 1 token\n- **Letti:** fixture, servita\n", encoding="utf-8")
                self.git(root, "add", new)
                result = self.git(root, "commit", "-m", "nota valida", "--", new)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual((root / "raw/sessioni/2020-01-01-storica.md").read_text(), "# Nota storica\n")

    def test_nota_nuova_invalida_resta_bloccata(self):
        for linked in (False, True):
            with self.subTest(linked=linked), tempfile.TemporaryDirectory() as tmp:
                root = self.prepara(Path(tmp), linked)
                new = "raw/sessioni/2020-01-02-invalida.md"
                (root / new).write_text("# Senza costo e letture\n", encoding="utf-8")
                self.git(root, "add", new)
                result = self.git(root, "commit", "-m", "nota invalida", "--", new)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("invalida.md", result.stdout + result.stderr)
                self.assertIn("Letti", result.stdout + result.stderr)

    def test_modifica_nota_storica_resta_bloccata(self):
        for linked in (False, True):
            with self.subTest(linked=linked), tempfile.TemporaryDirectory() as tmp:
                root = self.prepara(Path(tmp), linked)
                old = "raw/sessioni/2020-01-01-storica.md"
                (root / old).write_text("# Modifica vietata\n", encoding="utf-8")
                self.git(root, "add", old)
                result = self.git(root, "commit", "-m", "modifica vietata", "--", old)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("immutabile", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
