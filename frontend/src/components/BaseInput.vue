<template>
  <div class="form-group">
    <label for="addTodo" class="control-label">Add todo</label>
    <input
      :value="value"
      v-on:input="$emit('input', $event.target.value)"
      v-on:keyup.enter="$emit('add-todo')"
      class="form-control"
      type="text"
      id='addTodo'
    />
  </div>
</template>

<script>
export default {
  props: {
    value: String,
  },
};
</script>

<style scoped>

</style>
