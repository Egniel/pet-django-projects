<template>
    <div class="col-lg-3">
      <BaseInput
      v-model="inputPhoneNumber"
      v-bind="{inputText:'Find client'}"
      @add-todo="addTodo()" ></BaseInput>
      <client-card
        v-if="clientObject"
        :client=clientObject
      ></client-card>
    </div>
</template>

<script>

import BaseInput from './BaseInput';
import ClientCard from './ClientCard';

export default {
  components: {
    BaseInput, ClientCard,
  },
  data() {
    return {
      inputPhoneNumber: '',
      clientObject: undefined,
    };
  },
  methods: {
    addTodo() {
      this.clientObject = this.$store.state.clients[this.inputPhoneNumber];
      this.inputPhoneNumber = '';
      return this.clientObject;
    },
  },
};
</script>

<style scoped>

</style>
