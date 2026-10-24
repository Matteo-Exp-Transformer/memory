/* Palestra — calcolatore di espressioni sicuro (niente eval).
 * Da copiare TALE E QUALE dentro palestra.html, in un <script>, prima del codice della pagina.
 *
 * Uso:
 *   Espressioni.calcola("ceil(domanda / capacita * 60)", {domanda: 90, capacita: 4})  -> numero
 *   Espressioni.variabili("min(a, b) + 2")                                             -> ["a", "b"]
 *   Espressioni.formatta(3.14159, 1)                                                   -> "3,1"
 *
 * Linguaggio: numeri (3, 2.5), variabili (lettere, cifre, _), + - * / ( ) ,
 * confronti < <= > >= == != (danno 1 o 0), funzioni: min max ceil floor round abs se(cond, a, b).
 * Divisione per zero = Infinity (la pagina la mostra come «∞»).
 * Errori: lancia Error con messaggio in italiano.
 */
(function (radice) {
  "use strict";

  var FUNZIONI = {
    min: { n: -1, f: function (a) { return Math.min.apply(null, a); } },
    max: { n: -1, f: function (a) { return Math.max.apply(null, a); } },
    ceil: { n: 1, f: function (a) { return Math.ceil(a[0]); } },
    floor: { n: 1, f: function (a) { return Math.floor(a[0]); } },
    round: { n: 1, f: function (a) { return Math.round(a[0]); } },
    abs: { n: 1, f: function (a) { return Math.abs(a[0]); } },
    se: { n: 3, f: function (a) { return a[0] !== 0 ? a[1] : a[2]; } }
  };

  function tokenizza(testo) {
    if (typeof testo !== "string") throw new Error("l'espressione deve essere un testo");
    var t = [], i = 0, c;
    while (i < testo.length) {
      c = testo[i];
      if (c === " " || c === "\t" || c === "\n") { i++; continue; }
      if (/[0-9.]/.test(c)) {
        var j = i;
        while (j < testo.length && /[0-9.]/.test(testo[j])) j++;
        var s = testo.slice(i, j);
        if (!/^(\d+\.?\d*|\.\d+)$/.test(s)) throw new Error("numero non valido: " + s);
        t.push({ k: "num", v: parseFloat(s) }); i = j; continue;
      }
      if (/[A-Za-z_]/.test(c)) {
        var k = i;
        while (k < testo.length && /[A-Za-z0-9_]/.test(testo[k])) k++;
        t.push({ k: "id", v: testo.slice(i, k) }); i = k; continue;
      }
      var due = testo.slice(i, i + 2);
      if (due === "<=" || due === ">=" || due === "==" || due === "!=") { t.push({ k: "op", v: due }); i += 2; continue; }
      if ("+-*/(),<>".indexOf(c) >= 0) { t.push({ k: "op", v: c }); i++; continue; }
      throw new Error("carattere non ammesso: «" + c + "»");
    }
    return t;
  }

  // Grammatica:  confronto := somma (opConfronto somma)?
  //              somma := prodotto (('+'|'-') prodotto)*
  //              prodotto := unario (('*'|'/') unario)*
  //              unario := '-' unario | primario
  //              primario := num | id | id '(' args ')' | '(' confronto ')'
  function analizza(testo) {
    var t = tokenizza(testo), p = 0;
    function guarda() { return t[p]; }
    function prendi(v) {
      var x = t[p];
      if (!x || x.v !== v) throw new Error("atteso «" + v + "»" + (x ? " invece di «" + x.v + "»" : " alla fine"));
      p++;
    }
    function confronto() {
      var a = somma(), x = guarda();
      if (x && x.k === "op" && ["<", "<=", ">", ">=", "==", "!="].indexOf(x.v) >= 0) {
        p++; return { k: "cmp", op: x.v, a: a, b: somma() };
      }
      return a;
    }
    function somma() {
      var a = prodotto(), x;
      while ((x = guarda()) && x.k === "op" && (x.v === "+" || x.v === "-")) { p++; a = { k: "bin", op: x.v, a: a, b: prodotto() }; }
      return a;
    }
    function prodotto() {
      var a = unario(), x;
      while ((x = guarda()) && x.k === "op" && (x.v === "*" || x.v === "/")) { p++; a = { k: "bin", op: x.v, a: a, b: unario() }; }
      return a;
    }
    function unario() {
      var x = guarda();
      if (x && x.k === "op" && x.v === "-") { p++; return { k: "neg", a: unario() }; }
      return primario();
    }
    function primario() {
      var x = guarda();
      if (!x) throw new Error("espressione incompleta");
      if (x.k === "num") { p++; return { k: "num", v: x.v }; }
      if (x.k === "id") {
        p++;
        var y = guarda();
        if (y && y.v === "(") {
          var fn = FUNZIONI[x.v];
          if (!fn) throw new Error("funzione sconosciuta: " + x.v);
          p++;
          var args = [];
          if (guarda() && guarda().v !== ")") {
            args.push(confronto());
            while (guarda() && guarda().v === ",") { p++; args.push(confronto()); }
          }
          prendi(")");
          if (fn.n >= 0 && args.length !== fn.n) throw new Error(x.v + " vuole " + fn.n + " argomenti");
          if (fn.n < 0 && args.length < 1) throw new Error(x.v + " vuole almeno un argomento");
          return { k: "fn", nome: x.v, args: args };
        }
        if (FUNZIONI[x.v]) throw new Error(x.v + " è una funzione: usala con le parentesi");
        return { k: "var", nome: x.v };
      }
      if (x.v === "(") { p++; var e = confronto(); prendi(")"); return e; }
      throw new Error("simbolo inatteso: «" + x.v + "»");
    }
    var albero = confronto();
    if (p < t.length) throw new Error("simbolo in più: «" + t[p].v + "»");
    return albero;
  }

  function valuta(n, vars) {
    switch (n.k) {
      case "num": return n.v;
      case "var":
        if (!Object.prototype.hasOwnProperty.call(vars, n.nome)) throw new Error("variabile sconosciuta: " + n.nome);
        var v = Number(vars[n.nome]);
        if (isNaN(v)) throw new Error("la variabile " + n.nome + " non è un numero");
        return v;
      case "neg": return -valuta(n.a, vars);
      case "bin":
        var a = valuta(n.a, vars), b = valuta(n.b, vars);
        if (n.op === "+") return a + b;
        if (n.op === "-") return a - b;
        if (n.op === "*") return a * b;
        return b === 0 ? (a === 0 ? 0 : Infinity) : a / b;
      case "cmp":
        var x = valuta(n.a, vars), y = valuta(n.b, vars), r;
        if (n.op === "<") r = x < y; else if (n.op === "<=") r = x <= y;
        else if (n.op === ">") r = x > y; else if (n.op === ">=") r = x >= y;
        else if (n.op === "==") r = x === y; else r = x !== y;
        return r ? 1 : 0;
      case "fn":
        if (n.nome === "se") { return valuta(n.args[0], vars) !== 0 ? valuta(n.args[1], vars) : valuta(n.args[2], vars); }
        return FUNZIONI[n.nome].f(n.args.map(function (q) { return valuta(q, vars); }));
    }
    throw new Error("nodo sconosciuto");
  }

  function raccogli(n, out) {
    if (n.k === "var" && out.indexOf(n.nome) < 0) out.push(n.nome);
    if (n.a) raccogli(n.a, out);
    if (n.b) raccogli(n.b, out);
    if (n.args) n.args.forEach(function (q) { raccogli(q, out); });
    return out;
  }

  radice.Espressioni = {
    calcola: function (testo, variabili) { return valuta(analizza(testo), variabili || {}); },
    variabili: function (testo) { return raccogli(analizza(testo), []); },
    controlla: function (testo) { analizza(testo); return true; },
    formatta: function (numero, decimali) {
      if (numero === Infinity) return "∞";
      if (numero === -Infinity) return "-∞";
      if (typeof numero !== "number" || isNaN(numero)) return "—";
      var d = typeof decimali === "number" ? decimali : 1;
      return numero.toFixed(d).replace(".", ",");
    }
  };
})(typeof window !== "undefined" ? window : globalThis);
