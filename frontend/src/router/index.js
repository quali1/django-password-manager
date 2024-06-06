import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/ui/pages/Home/HomeView";
import LoginView from "@/ui/pages/Login/LoginView";
import RegistrationView from "@/ui/pages/Registration/RegistrationView";

const routes = [
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/registration",
    name: "registration",
    component: RegistrationView,
  },
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
