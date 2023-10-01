function Prime(s) {
  if (s<=1) {
    return false;
  }
  for (let i=2;i<s;i++) {
    if (s%i===0) {
      return false;
    }
  }
  return true;
}
const read = require('readline');
const r= read.createInterface({
  input: process.stdin,
  output: process.stdout
});
r.question("Enter n: ", input => {
  const n = parseInt(input);
  console.log("Prime numbers: ");
  for (let i=2;i<=n;i++) {
      if (Prime(i)) {
          process.stdout.write(i+", ");
      }
  }
  r.close();
});
