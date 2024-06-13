import { createRouter, createWebHistory } from "vue-router";

import HomeView from "@/ui/pages/Home/HomeView";
import HomeAddPasswordContent from "@/ui/pages/Home/Content/HomeAddPasswordContent";
import HomeAddProfileContent from "@/ui/pages/Home/Content/HomeAddProfileContent";
import HomeDefaultContent from "@/ui/pages/Home/Content/HomeDefaultContent";
import LoginView from "@/ui/pages/Login/LoginView";
import RegistrationView from "@/ui/pages/Registration/RegistrationView";

const routes = [
  {
    path: "/login",
    name: "login",
    component: LoginView,
    meta: { auth: true },
  },
  {
    path: "/registration",
    name: "registration",
    component: RegistrationView,
    meta: { auth: true },
  },
  {
    path: "/",
    component: HomeView,
    children: [
      {
        path: "",
        name: "home",
        component: HomeDefaultContent,
      },
      {
        path: "add-password",
        name: "add-password",
        component: HomeAddPasswordContent,
      },
      {
        path: "add-profile",
        name: "add-profile",
        component: HomeAddProfileContent,
      },
    ],
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
