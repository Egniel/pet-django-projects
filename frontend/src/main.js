// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import Vuex from 'vuex';
import App from './App';
import router from './router';

Vue.use(Vuex);
Vue.config.productionTip = false;

// eslint-disable-next-line
const store = new Vuex.Store({
  state: {
    clients: {
      89062601337: {
        name: 'David',
        visits: 10,
      },
      89531623083: {
        name: 'Ira',
        visits: 100,
      },
      89112474074: {
        name: 'Mama',
        visits: 0,
      },
    },
  },
  mutations: {
    increment(state) {
      // eslint-disable-next-line
      state.count++;
    },
  },
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
