function randomDate(start, end) {
  return new Date(
    start.getTime() + Math.random() * (end.getTime() - start.getTime())
  );
}

/*randomDate(new Date(2021, 0, 1), new Date(2021, 12, 31));*/

export function randomData() {
  const date = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ];
  let nbTh = [];
  let nbRel = [];
  for (let i = 0; i < date.length; i++) {
    nbTh.push(Math.floor(Math.random() * 1000) + 100);
    nbRel.push(Math.floor(Math.random() * 10) + 1);
  }
  return [date, nbTh, nbRel];
}
