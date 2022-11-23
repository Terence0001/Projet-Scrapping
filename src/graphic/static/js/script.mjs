import { randomData } from "./randomData.mjs";
//import { moveScroll } from "./fonctions.mjs";

let [date, nbTh, nbRel] = randomData();
const ctx = document.getElementById("barCanvas");

/* ------------------------ BAR --------------------- */
const barChart = {
  type: "bar",
  yAxisID: "y",
  label: "Weekly Sales",
  data: nbTh,
  backgroundColor: [
    "rgba(255, 26, 104, 0.2)",
    "rgba(54, 162, 235, 0.2)",
    "rgba(255, 206, 86, 0.2)",
    "rgba(75, 192, 192, 0.2)",
    "rgba(153, 102, 255, 0.2)",
    "rgba(255, 159, 64, 0.2)",
    "rgba(0, 0, 0, 0.2)"
  ],
  borderColor: [
    "rgba(255, 26, 104, 1)",
    "rgba(54, 162, 235, 1)",
    "rgba(255, 206, 86, 1)",
    "rgba(75, 192, 192, 1)",
    "rgba(153, 102, 255, 1)",
    "rgba(255, 159, 64, 1)",
    "rgba(0, 0, 0, 1)"
  ],
  borderWidth: 1,
  order: 2
};

/* ------------------------ LINE --------------------- */
const lineChart = {
  type: "line",
  label: "Line Dataset",
  data: nbRel,
  yAxisID: "rel",
  order: 1,
  tension: 0.4
};

/* ------------------------ SCALE --------------------- */
const scalesChart = {
  x: {
    min: 0,
    max: 6
  },
  y: {
    type: "linear",
    position: "left",
    beginAtZero: true,
    suggestedMin: 0,
    suggestedMax: Math.max(...nbTh) + 10
  },
  rel: {
    type: "linear",
    position: "right",
    beginAtZero: true,
    display: true,
    suggestedMin: 0,
    suggestedMax: Math.max(...nbRel) + 3,
    grid: {
      display: false
    }
  }
};

/* ------------------------ PLUGINS --------------------- */

const moveChart = {
  id: "moveChart",
  afterEvent(chart, args) {
    const {
      ctx,
      canvas,
      chartArea: { left, right, top, bottom, width, height }
    } = chart;
    canvas.addEventListener("mousemove", (event) => {
      //console.log(event);
      // MOUSE COORDINATE
      const x = args.event.x;
      const y = args.event.y;
      if (
        x >= left - 15 &&
        x <= left + 15 &&
        y >= height / 2 + top - 15 &&
        y <= height / 2 + top + 15
      ) {
        canvas.style.cursor = "pointer";
      } else if (
        x >= right - 15 &&
        x <= right + 15 &&
        y >= height / 2 + top - 15 &&
        y <= height / 2 + top + 15
      ) {
        canvas.style.cursor = "pointer";
      } else {
        canvas.style.cursor = "default";
      }
    });
  },
  afterDraw(chart, args, pluginOptions) {
    const {
      ctx,
      chartArea: { left, right, top, bottom, width, height }
    } = chart;

    class CircleChevron {
      draw(ctx, x1, pixel) {
        const angle = Math.PI / 180;
        // Left Part
        ctx.beginPath();
        ctx.lineWidth = 3;
        ctx.strokeStyle = "rgba(102, 102, 102, 0.5)";
        ctx.fillStyle = "white";
        ctx.arc(x1, height / 2 + top, 10, angle * 0, angle * 360, false);
        ctx.stroke();
        ctx.fill();
        ctx.closePath();
        // chevron arrow left
        ctx.beginPath();
        ctx.lineWidth = 3;
        ctx.strokeStyle = "rgba(255, 26, 104, 1)";
        ctx.moveTo(x1 + pixel, height / 2 + top - 7.5);
        ctx.lineTo(x1 - pixel, height / 2 + top);
        ctx.lineTo(x1 + pixel, height / 2 + top + 7.5);
        ctx.stroke();
        ctx.closePath();
      }
    }
    let drawCircleLeft = new CircleChevron();
    drawCircleLeft.draw(ctx, left, 5);
    let drawCircleRight = new CircleChevron();
    drawCircleRight.draw(ctx, right, -5);
  }
};

/* OPTIONS */

/* ------------------------------------------------------------- */

const mixedChart = new Chart(ctx, {
  data: {
    datasets: [barChart, lineChart],
    labels: date
  },
  options: {
    layout: {
      padding: {
        right: 18
      }
    },
    scales: scalesChart,
    plugins: {
      datalabels: {
        anchor: "end",
        align: "top"
      }
    }
  },
  plugins: [ChartDataLabels, moveChart]
});

function moveScroll() {
  const {
    ctx,
    canvas,
    chartArea: { left, right, top, bottom, width, height }
  } = mixedChart;
  canvas.addEventListener("click", (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    if (
      x >= right - 15 &&
      x <= right + 15 &&
      y >= height / 2 + top - 15 &&
      y <= height / 2 + top + 15
    ) {
      mixedChart.options.scales.x.min = mixedChart.options.scales.x.min + 7;
      mixedChart.options.scales.x.max = mixedChart.options.scales.x.max + 7;
      if (mixedChart.options.scales.x.max >= barChart.data.length) {
        mixedChart.options.scales.x.min = barChart.data.length - 7;
        mixedChart.options.scales.x.max = barChart.data.length;
        /* barChart.data = newData
        lineChart.data = newData */
      }
    }
    if (
      x >= left - 15 &&
      x <= left + 15 &&
      y >= height / 2 + top - 15 &&
      y <= height / 2 + top + 15
    ) {
      mixedChart.options.scales.x.min = mixedChart.options.scales.x.min - 7;
      mixedChart.options.scales.x.max = mixedChart.options.scales.x.max - 7;
      if (mixedChart.options.scales.x.min <= 0) {
        mixedChart.options.scales.x.min = 0;
        mixedChart.options.scales.x.max = 6;
        /* barChart.data = newData
         lineChart.data = newData */
      }
    }
    mixedChart.update();
  });
}

mixedChart.ctx.onclick = moveScroll();
