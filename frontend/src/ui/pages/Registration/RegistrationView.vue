<template>
  <auth-layout>
    <template #inputs>
      <input-component v-model="username" placeholder="Username" />
      <input-component v-model="password" placeholder="Password" :hide="true" />
    </template>
    <template #buttons>
      <button-component @click="singUp">SingUp</button-component>
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
    singUp() {
      this.$store.commit("auth/singUp");
      this.$router.push({ name: "login" });
    },
  },
};
</script>
