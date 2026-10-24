// Prova del calcolatore. Uso: node palestra/motore/prova_espressioni.mjs  (deve stampare «tutto ok»)
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const qui = dirname(fileURLToPath(import.meta.url));
new Function(readFileSync(join(qui, "espressioni.js"), "utf8"))();
const E = globalThis.Espressioni;

let errori = 0;
function uguale(espr, vars, atteso) {
  const r = E.calcola(espr, vars);
  if (!(r === atteso || Math.abs(r - atteso) < 1e-9)) { errori++; console.log("SBAGLIATO", espr, "=", r, "atteso", atteso); }
}
function errore(espr, vars) {
  try { E.calcola(espr, vars); errori++; console.log("DOVEVA DARE ERRORE", espr); } catch (e) { /* giusto */ }
}

uguale("1 + 2 * 3", {}, 7);
uguale("(1 + 2) * 3", {}, 9);
uguale("-2 + 5", {}, 3);
uguale("10 / 4", {}, 2.5);
uguale("1 / 0", {}, Infinity);
uguale("ceil(domanda / capacita)", { domanda: 9, capacita: 4 }, 3);
uguale("min(a, b, 7)", { a: 9, b: 8 }, 7);
uguale("max(a, b)", { a: 9, b: 8 }, 9);
uguale("se(carico >= 1, 999, carico * 10)", { carico: 0.5 }, 5);
uguale("se(carico >= 1, 999, carico * 10)", { carico: 1.2 }, 999);
uguale("round(2.5) + floor(2.9) + abs(-1)", {}, 6);
uguale("60 / somma * 6", { somma: 71 }, 360 / 71);
errore("2 +", {});
errore("x * 2", {});
errore("alert(1)", {});
errore("a; b", { a: 1, b: 2 });
errore("ceil(1, 2)", {});
errore("window", {});
const v = E.variabili("min(a, b) + se(c > 1, a, 2)");
if (v.join(",") !== "a,b,c") { errori++; console.log("variabili sbagliate", v); }
if (E.formatta(Infinity) !== "∞" || E.formatta(3.14159, 1) !== "3,1") { errori++; console.log("formatta sbagliato"); }

console.log(errori ? `${errori} errori` : "tutto ok");
process.exit(errori ? 1 : 0);
