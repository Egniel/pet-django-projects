import Vue from 'vue';
import Router from 'vue-router';
import TodoItemList from '@/components/TodoItemList';
import IndexView from '@/views/IndexView';
// import test from '@/components/test';
import VueResource from 'vue-resource';

Vue.use(VueResource);
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/todo',
      name: 'TodoItemList',
      component: TodoItemList,
    },
    {
      path: '/',
      name: 'IndexView',
      component: IndexView,
    },
    // {
    //   path: '/test',
    //   name: 'test',
    //   component: test,
    // },
  ],
});
