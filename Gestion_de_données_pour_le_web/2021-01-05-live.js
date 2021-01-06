// SELECT DISTINCT * FROM R;
function map_q1() {
  if (this.value.rel === "R") {
    emit({ A: this.value.A, B: this.value.B }, null);
  }
}

function red_q1(k, vs) {
  return null;
}

// SELECT A, COUNT(*) FROM R GROUP BY A;
function map_q2() {
  if (this.value.rel === "R") {
    emit(this.value.A, 1);
  }
}

function red_q2(k, vs) {
  return Array.sum(vs);
}

// SELECT * FROM R UNION SELECT X as A, Y as B FROM S;
function map_q3() {
  if (this.value.rel === "R") {
    emit({ A: this.value.A, B: this.value.B }, null);
  } else if (this.value.rel === "S") {
    emit({ A: this.value.X, B: this.value.Y }, null);
  }
}

function red_q3(k, vs) {
  return null;
}

// SELECT * FROM R UNION ALL SELECT X as A, Y as B FROM S;
function map_q3_all() {
  if (this.value.rel === "R") {
    emit(this._id, { A: this.value.A, B: this.value.B });
  } else if (this.value.rel === "S") {
    emit(this._id, { A: this.value.X, B: this.value.Y });
  }
}

function red_q3_all(k, vs) {
  return undefined;
}

// SELECT * FROM R INTERSECT SELECT X as A, Y as B FROM S;
function map_q4() {
  if (this.value.rel === "R") {
    emit({ A: this.value.A, B: this.value.B }, { R: 1, S: 0 });
  } else if (this.value.rel === "S") {
    emit({ A: this.value.X, B: this.value.Y }, { R: 0, S: 1 });
  }
}

function red_q4(k, vs) {
  // tester si dans vs on a bien la preuve que k vient de R et vient de S
  let in_R = false;
  let in_S = false;
  for (let i = 0; i < vs.length; i += 1) {
    in_R = in_R || vs[i].R;
    in_S = in_S || vs[i].S;
  }
  return { R: in_R, S: in_S };
}

// SELECT * FROM R WHERE A < 1;
function map_q5() {
  if (this.value.rel === "R" && this.value.A < 1) {
    emit({ id: this._id, A: this.value.A, B: this.value.B }, null);
  }
}

function red_q5(k, vs) {
  return undefined;
}
