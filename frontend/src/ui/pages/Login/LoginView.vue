<template>
  <auth-layout>
    <template #inputs>
      <input-component
        :class="{
          'input-error': !username && isError,
        }"
        v-model="username"
        placeholder="Username"
      />
      <input-component
        :class="{
          'input-error': !password && isError,
        }"
        v-model="password"
        placeholder="Password"
        :hide="true"
        @keyup.enter="submit()"
      />
    </template>
    <template #buttons>
      <button-component @click="submit()">Login</button-component>
    </template>
    <template #errors>
      <expandable-component class="error-log" :active="isError">
        <div class="container">{{ error }}</div>
      </expandable-component>
    </template>
    <template #links>
      <router-link :to="{ name: 'registration' }">
        Don't have an account?<br />
        Register here
      </router-link>
    </template>
  </auth-layout>
</template>

<script>
import { mapState, mapActions } from "vuex";

import InputComponent from "@/ui/components/InputComponent";
import ButtonComponent from "@/ui/components/ButtonComponent";
import ExpandableComponent from "@/ui/components/ExpandableComponent";
import AuthLayout from "@/ui/layouts/AuthLayout";

export default {
  components: {
    InputComponent,
    ButtonComponent,
    ExpandableComponent,
    AuthLayout,
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  computed: {
    ...mapState("auth", ["error", "isError"]),
  },
  methods: {
    ...mapActions("auth", ["login", "setError", "clearError"]),
    submit() {
      if (!(this.username && this.password)) {
        this.setError("Fill in all the fields!");
      } else {
        this.login([this.username, this.password]);
      }
    },
  },
  mounted() {
    this.clearError();
  },
};
</script>

<style lang="scss" scoped>
.error-log:not(.active) {
  opacity: 0;
}

.input-error > * {
  color: $red-color;
}

.container {
  height: calc($gap * 2 - 8px + 18px);
}
</style>
