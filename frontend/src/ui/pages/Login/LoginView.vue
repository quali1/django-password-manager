<template>
  <auth-layout>
    <template #inputs>
      <input-component
        :error="!username && isError"
        v-model="username"
        placeholder="Username"
      />
      <input-component
        v-model="password"
        placeholder="Password"
        :error="!password && isError"
        :hide="true"
        @keyup.enter="submit"
      />
    </template>
    <template #buttons>
      <button-component @click="submit">Login</button-component>
    </template>
    <template #errors>
      <error-component />
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
      password: "",
    };
  },
  computed: {
    ...mapState("error", ["isError"]),
  },
  methods: {
    ...mapActions("auth", ["login"]),
    ...mapActions("error", ["setError"]),
    submit() {
      if (!(this.username && this.password)) {
        this.setError("Fill in all the fields!");
      } else {
        this.login([this.username, this.password]);
      }
    },
  },
};
</script>
