<template>
  <div>
    <div v-if="process.client">
      <div ref="chart"></div>
    </div>
    <div v-else>
      Loading chart...
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import * as Plotly from 'plotly.js-dist-min';

export default {
  mounted() {
    if (process.client) {
      this.loadChart();
    }
  },
  methods: {
    async loadChart() {
      try {
        const ohlcResponse = await axios.get('http://127.0.0.1:8000/ohlc');
        const ema20Response = await axios.get('http://127.0.0.1:8000/ema?period=20');
        const ema50Response = await axios.get('http://127.0.0.1:8000/ema?period=50');
        const ema100Response = await axios.get('http://127.0.0.1:8000/ema?period=100');
        const ema200Response = await axios.get('http://127.0.0.1:8000/ema?period=200');

        const ohlcData = ohlcResponse.data.data;
        const ema20 = ema20Response.data;
        const ema50 = ema50Response.data;
        const ema100 = ema100Response.data;
        const ema200 = ema200Response.data;

        const timestamps = ohlcData.map(item => item.timestamp);
        const ohlcCloseValues = ohlcData.map(item => item.close);

        const traceOhlc = {
          x: timestamps,
          y: ohlcCloseValues,
          type: 'scatter',
          mode: 'lines',
          name: 'OHLC Close'
        };

        const traceEma20 = {
          x: timestamps,
          y: ema20,
          type: 'scatter',
          mode: 'lines',
          name: 'EMA 20'
        };

        const traceEma50 = {
          x: timestamps,
          y: ema50,
          type: 'scatter',
          mode: 'lines',
          name: 'EMA 50'
        };

        const traceEma100 = {
          x: timestamps,
          y: ema100,
          type: 'scatter',
          mode: 'lines',
          name: 'EMA 100'
        };

        const traceEma200 = {
          x: timestamps,
          y: ema200,
          type: 'scatter',
          mode: 'lines',
          name: 'EMA 200'
        };

        const data = [traceOhlc, traceEma20, traceEma50, traceEma100, traceEma200];

        const layout = {
          title: 'OHLC Data with EMA Lines',
          xaxis: { title: 'Timestamp' },
          yaxis: { title: 'Value' }
        };

        Plotly.newPlot(this.$refs.chart, data, layout);
      } catch (error) {
        console.error('Error loading chart data:', error);
      }
    }
  }
}
</script>

<style scoped>
/* Add your styles here */
</style>
