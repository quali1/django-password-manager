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
          'input-error': !email && isError,
        }"
        v-model="email"
        placeholder="Email"
      />
      <input-component
        :class="{
          'input-error': !password && isError,
        }"
        v-model="password"
        placeholder="Password"
        @keyup.enter="submit()"
        :hide="true"
      />
      <input-component
        :class="{
          'input-error': !confirmPassword && isError,
        }"
        v-model="confirmPassword"
        placeholder="Confirm password"
        @keyup.enter="submit()"
        :hide="true"
      />
    </template>
    <template #buttons>
      <button-component @click="submit()">SingUp</button-component>
    </template>
    <template #errors>
      <expandable-component class="error-log" :active="isError">
        <div class="container">{{ error }}</div>
      </expandable-component>
    </template>
    <template #links>
      <router-link :to="{ name: 'login' }">
        Already have an account?<br />
        Login here
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
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  computed: {
    ...mapState("auth", ["error", "isError"]),
  },
  methods: {
    ...mapActions("auth", ["signUp", "setError", "clearError"]),
    submit() {
      if (
        !(this.username && this.email && this.password && this.confirmPassword)
      ) {
        this.setError("Fill in all the fields!");
      } else if (this.password !== this.confirmPassword) {
        this.setError("Passwords should be equal!");
      } else {
        this.signUp([this.username, this.email, this.password]);
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
