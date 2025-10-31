class Vector {

  count: number;
  size: number;
  data: number[];
  #EXPAND_RATIO: number = 2;

  constructor(n: number) {
    if (!Number.isInteger(n)) {
      throw Error("The size of a vector must be integer.");
    }
    this.count = 0;
    this.size = n;
    this.data = new Array(n).fill(0);
  }

  insert(pos: number, n: number): 0 | 1 {
    if (!Number.isInteger(pos) || !Number.isInteger(n)) {
      throw Error("Either parameter pos or n must be integer.");
    }
    if (pos < 0 || pos > this.count) {
      return 0;
    }
    if (this.count === this.size) {
      this.#expand();
    }
    for (let i = this.count - 1; i > pos; i--) {
      this.data[i] = this.data[i - 1];
    }
    this.data[pos] = n;
    this.count += 1;
    return 1;
  }

  remove(pos: number): 0 | 1 {
    if (!Number.isInteger(pos)) {
      throw Error("parameter pos must be integer.");
    }
    if (pos < 0 || pos >= this.count) {
      return 0;
    }
    for (let i = pos; i < this.count - 1; i++) {
      this.data[i] = this.data[i + 1];
    }
    for (let i = this.count - 1; i < this.size; i++) {
      this.data[i] = 0;
    }
    this.count -= 1;
    return 1;
  }

  toString() {
    return this.#formatVector();
  }

  [Symbol.toPrimitive](hint: "string" | "number" | "default") {
    if (hint === 'string' || hint === 'default') {
      return this.#formatVector();
    }
    return this.size;
  }

  [Symbol.for('nodejs.util.inspect.custom')]() {
    return this.#formatVector();
  }


  #expand() {
    const newSize = this.size * this.#EXPAND_RATIO;
    const newData = new Array(newSize).fill(0);

    for (let i = 0; i < this.size; i++) {
      newData[i] = this.data[i];
    }

    this.data = newData;
    this.size = newSize;
  }

  #formatVector(): string {
    const widths: number[] = [];
    for (let i = 0; i < this.size; i++) {
      widths[i] = Math.max(String(i).length, String(this.data[i]).length);
    }

    const totalWidth = widths.reduce((sum, w) => sum + w, 0) + (this.size - 1);
    const result: string[] = [];

    result.push(`┌─${'─'.repeat(totalWidth)}─┐`);

    let indexLine = '│ ';
    for (let i = 0; i < this.size; i++) {
      indexLine += String(i).padStart(widths[i], ' ') + (i < this.size - 1 ? ' ' : '');
    }
    result.push(indexLine + ' │');

    result.push(`├─${'─'.repeat(totalWidth)}─┤`);

    let dataLine = '│ ';
    for (let i = 0; i < this.size; i++) {
      dataLine += String(this.data[i]).padStart(widths[i], ' ') + (i < this.size - 1 ? ' ' : '');
    }
    result.push(dataLine + ' │');

    result.push(`└─${'─'.repeat(totalWidth)}─┘`);

    return result.join('\n');
  }
}

(function () {
  const MAX_OPS = 20;
  const VECTOR_LENGTH = 2;
  const N_MAX = 10000;
  const INSERT_RATIO = 80;
  const POSITION_OVERFLOW = 3;

  const vector = new Vector(VECTOR_LENGTH);

  for (let i = 0; i < MAX_OPS; i++) {
    const op = Math.floor(1 + Math.random() * 100);
    const pos = Math.floor(Math.random() * (vector.count + POSITION_OVERFLOW));

    if (op < INSERT_RATIO) {
      const n = Math.floor(1 + Math.random() * N_MAX);
      console.log(`insert ${n} at position ${pos} to vector = ${vector.insert(pos, n)}`);
    } else {
      console.log(`remove at position ${pos} from vector = ${vector.remove(pos)}`);
    }
    console.log(vector);
  }
})();

