<template>
    <div class=container>
        <div class="list-group">
        <a href="#/currencies" class="list-group-item list-group-item-action
        flex-column align-items-start">
            <div class="d-flex w-100 justify-content-between">
            <h5 class="mb-1">List group item heading</h5>
            <small>3 days ago</small>
            </div>
            <p class="mb-1">Donec id elit non mi porta gravida at eget metus.
              Maecenas sed diam eget risus varius blandit.</p>
            <small>Donec id elit non mi porta.</small>
        </a>
        </div>
        <div class="list-group">
        <a href="#/currencies" class="list-group-item list-group-item-action
        flex-column align-items-start">
            <div class="d-flex w-100 justify-content-between">
            <h5 class="mb-1">{{ digital_currency_code }} / {{ market_code }}</h5>
            <small>{{ dates[0].time }}</small>
            </div>
            <p class="mb-1">Donec id elit non mi porta gravida at eget metus.
              Maecenas sed diam eget risus varius blandit.</p>
            <small>Donec id elit non mi porta.</small>
        </a>
        {{ dates[0].time }}
        </div>
    </div>
</template>

<script>
    export default {
      data() {
        return {
          'information': 'Intraday Prices and Volumes for Digital Currency',
          'digital_currency_code': 'BTC',
          'digital_currency_name': 'Bitcoin',
          'market_code': 'ETH',
          'market_name': 'Ethereum',
          'interval': '5min',
          'last_refreshed': '2018-07-28 09:00:00',
          'time_zone': 'UTC',
          'dates': [{
            'time': '2018-07-28 08:55:00',
            'price_alt': '17.43283208 (ETH)',
            'price_usd': '8194.58365830 (USD)',
            'volume': '5284.05980391',
            'market_cap_usd': '43300670.11861300 (USD)'
        }]
        }
      },

    }
</script>

<style scoped>

</style>