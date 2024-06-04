<template>
  <auth-layout>
    <template #inputs>
      <input-component v-model="username" placeholder="Username" />
      <input-component v-model="password" placeholder="Password" :hide="true" />
    </template>
    <template #buttons>
      <button-component @click="login">Login</button-component>
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
import InputComponent from "@/ui/components/InputComponent";
import ButtonComponent from "@/ui/components/ButtonComponent";
import AuthLayout from "@/ui/layouts/AuthLayout";

export default {
  components: {
    InputComponent,
    ButtonComponent,
    AuthLayout,
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      this.$store.commit("auth/login");
      this.$router.push({ name: "home" });
    },
  },
};
</script>
