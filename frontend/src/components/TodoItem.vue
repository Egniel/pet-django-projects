<template>
  <li class="list-group-item d-flex justify-content-between align-items-center"
  :class="{active:isActive}"
  @mouseenter="hover"
  @mouseleave="hover"
  >
  <span v-if="todo.done"><s>{{ todo.text }}</s></span>
  <span v-else>{{ todo.text }}</span>
  <div class="text-center">
    <button
      v-show="displayRemoveButton"
      class="btn btn-outline-warning"
      @click="$emit('remove-todo')">
        X
    </button>
    <button
      v-show="isActive"
      class="btn btn-outline-success"
      @click="toggleDone(todo)">
        {{ buttonText }}
    </button>
  </div>
  </li>
</template>

<script>
export default {
  props: {
    todo: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      isActive: false,
    };
  },
  computed: {
    buttonText() {
      return this.todo.done ? 'Mark as undone' : 'Mark as done';
    },
    displayRemoveButton() {
      return this.todo.done && this.isActive;
    },
  },
  methods: {
    hover() {
      this.isActive = !this.isActive;
    },
    toggleDone() {
      this.todo.done = !this.todo.done;
    },
  },
};
</script>

<style scoped>
</style>
