<template>
  <div class="card text-white bg-primary text-center client-card">
    <div class="card-header">
      {{ client.name }}
    </div>
    <div class="card-body">
      {{ client.visits }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    client: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.client-card {
  height: 30vh;
}

</style>
