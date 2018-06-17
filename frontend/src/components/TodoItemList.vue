<template>
  <div class="container">
      <BaseInput v-model="inputTodo" @add-todo="addTodo()" ></BaseInput>
      <ul class="list-group">
        <TodoItem
          v-for="todo in todos"
          @remove-todo=removeTodo(todo)
          :todo="todo"
          :key="todo.id"
        ></TodoItem>
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
    // this.getTodos();
  },
  data() {
    return {
      inputTodo: '',
      todos: [
        {
          text: 'IRA',
          done: false,
        },
        {
          text: 'David',
          done: true,
        },
      ],
    };
  },
  methods: {
    getTodos() {
      this.loading = true;
      this.$http.get('/api/v1/todos/')
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
      if (this.inputTodo.length !== 0) {
        this.todos.push({
          text: this.inputTodo,
          done: false,
        });
        this.inputTodo = '';
      }
    },
    removeTodo(todo) {
      this.todos.splice(this.todos.indexOf(todo), 1);
    },
  },
};
</script>

<style>

</style>
