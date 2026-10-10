# BirthdaySim - Birthday Paradox Simulator

An interactive web-based simulator for the [Birthday Paradox](https://en.wikipedia.org/wiki/Birthday_problem) - the
surprising probability that two people in a group share the same birthday.

**[Play the live simulation here](https://akilary.github.io/BirthdayDataSimulator/)**

## What is the Birthday Paradox?

The Birthday Paradox states that in a group of just 23 people, there's roughly a 50% chance that two of them share a
birthday. By the time the group reaches 50 people, the probability jumps to over 97%. This feels counterintuitive, which
is why it's called a "paradox".

## Features

- Runs configurable Monte Carlo simulations directly in the browser
- Compares simulated empirical data against exact mathematical probability
- Generates a real-time interactive line graph using Chart.js
- Fully client-side with zero dependencies, local servers, or installation required
- Includes built-in dark and light themes

## Project Structure

```
BirthdayDataSimulator/
├── index.html
├── LICENSE
└── README.md
```

## Usage

No installation is required.

1. Simply open the `index.html` file in any modern web browser.
2. Enter your desired **Group size** and **Iterations**.
3. Click "Run Simulation" to generate the chart and see the exact probability metrics.

## Reference Probabilities

For context, here are the theoretical probabilities for various group sizes:

| Group Size | Probability of Match |
|------------|----------------------|
| 5          | ~2.7%                |
| 10         | ~11.7%               |
| 15         | ~25.5%               |
| 20         | ~41.2%               |
| 23         | ~50.8%               |
| 35         | ~81.4%               |
| 50         | ~97.1%               |

## Technologies Used

* Vanilla JavaScript (ES6)
* HTML5 / CSS3
* [Chart.js](https://www.chartjs.org/)

## License

[MIT](LICENSE)