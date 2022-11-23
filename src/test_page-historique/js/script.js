function randomDate(start, end) {
  return new Date(
    start.getTime() + Math.random() * (end.getTime() - start.getTime())
  );
}

export function randomData() {
  const options = {
    year: "numeric",
    month: "numeric",
    day: "numeric"
  };
  resL=[];
  for (let i = 0; i < 20; i++) {
    const l = [
      randomDate(new Date(2021, 0, 1), new Date(2021, 12, 31)).toLocaleDateString("fr-FR", options),
      Math.round(Math.random()),
      Math.floor(Math.random() * 50) + 10
    ]
    resL.push(l);
  }
  return resL
}