<template>
  <div>
    <span class="label">{{ todo.text }}</span>
  </div>
</template>

<script>
export default {
  props: {
    todo: {
      type: Object,
      required: true,
    },
  },
};
</script>
