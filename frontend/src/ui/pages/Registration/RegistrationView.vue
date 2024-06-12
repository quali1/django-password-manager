<template>
  <auth-layout>
    <template #inputs>
      <input-component
        :error="!username && isError"
        v-model="username"
        placeholder="Username"
      />
      <input-component
        :error="!email && isError"
        v-model="email"
        placeholder="Email"
      />
      <input-component
        :error="!password && isError"
        v-model="password"
        placeholder="Password"
        @keyup.enter="submit()"
        :hide="true"
      />
      <input-component
        :error="!confirmPassword && isError"
        v-model="confirmPassword"
        placeholder="Confirm password"
        @keyup.enter="submit()"
        :hide="true"
      />
    </template>
    <template #buttons>
      <button-component @click="submit">SingUp</button-component>
    </template>
    <template #errors>
      <error-component />
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
import ErrorComponent from "@/ui/components/ErrorComponent";
import AuthLayout from "@/ui/layouts/AuthLayout";

export default {
  components: {
    InputComponent,
    ButtonComponent,
    ErrorComponent,
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
    ...mapState("error", ["isError"]),
  },
  methods: {
    ...mapActions("auth", ["signUp"]),
    ...mapActions("error", ["setError"]),
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
};
</script>
