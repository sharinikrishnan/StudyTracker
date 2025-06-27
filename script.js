const form = document.getElementById("study-form");
const logList = document.getElementById("log-list");
const studyChart = document.getElementById("studyChart").getContext("2d");

let logs = [];

form.addEventListener("submit", function (e) {
  e.preventDefault();
  const date = document.getElementById("date").value;
  const subject = document.getElementById("subject").value;
  const hours = parseFloat(document.getElementById("hours").value);

  logs.push({ date, subject, hours });
  displayLogs();
  updateChart();
  form.reset();
});

function displayLogs() {
  logList.innerHTML = "";
  logs.forEach((log, index) => {
    const li = document.createElement("li");
    li.textContent = `${log.date}: ${log.subject} - ${log.hours} hours`;
    logList.appendChild(li);
  });
}

function updateChart() {
  const weeklyTotals = {};

  logs.forEach((log) => {
    if (!weeklyTotals[log.subject]) {
      weeklyTotals[log.subject] = 0;
    }
    weeklyTotals[log.subject] += log.hours;
  });

  const chartData = {
    labels: Object.keys(weeklyTotals),
    datasets: [{
      label: "Hours Studied",
      data: Object.values(weeklyTotals),
      backgroundColor: "rgba(75, 192, 192, 0.6)"
    }]
  };

  new Chart(studyChart, {
    type: "bar",
    data: chartData,
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}
