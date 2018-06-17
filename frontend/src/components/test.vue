<template>
  <div>
    <ul>
      <BaseInput v-model="inputTodo"></BaseInput>
      <TodoItem v-for="todo in todos" :todo="todo" :key="todo.id"></TodoItem>
    </ul>
  </div>
</template>

<script>

import TodoItem from './TodoItem';
import BaseInput from './BaseInput';

export default {
  components: {
    TodoItem, BaseInput,
  },
  mounted() {
    this.getTodos();
  },
  data() {
    return {
      inputTodo: '',
      todos: [],
    };
  },
  // computed: {
  //   todos: function() {
  //     var x = this.getTodos();
  //     console.log('asd',x);
  //     return x;
  //   }
  // },
  methods: {
    getTodos() {
      this.loading = true;
      this.$http.get('http://localhost:8000/api/v1/todos/')
        .then((response) => {
          this.todos = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          // eslint-disable-next-line
          console.log(err);
        });
    },
    addTodo() {
      console.log(this.todoText);
      this.todos.push({
        text: this.todoText,
      });
    },
  },
};
</script>

<style scoped>

</style>
