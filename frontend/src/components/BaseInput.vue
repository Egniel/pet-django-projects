<template>
  <div>
    <input v-model="todoText" type="text" placeholder="Text" v />
    <button @click="$emit('addTodo')">add todo</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todoText: '',
    };
  },
  methods: {
    addTodo() {
      console.log(this.todos);
      if (this.todoText.length !== 0) {
        this.todos.push({
          text: this.todoText,
        });
      }
    },
  },
};
</script>

<style scoped>

</style>
