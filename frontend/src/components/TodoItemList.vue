<template>
  <div>
    <ul>
      <TodoItem v-for="todo in todos" :todo="todo" :key="todo.id"></TodoItem>
    </ul>
  </div>
</template>

<script>
import TodoItem from './TodoItem';

export default {
  components: {
    TodoItem,
  },
  data() {
    return {
      todos: [
        {
          text: 'text1',
        },
        {
          text: 'text2',
        },
        {
          text: 'text3',
        },
      ],
    };
  },
  methods: {
  },
};
</script>

<style scoped>

</style>
