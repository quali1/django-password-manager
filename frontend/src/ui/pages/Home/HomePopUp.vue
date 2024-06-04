<template>
  <pop-up-component class="pop-up" :active="popUpActive">
    <template #content>
      <div class="header">
        <close-component class="close" @click="togglePopUp" />
      </div>
      <div class="content">
        <div class="main">
          <input-component
            class="username"
            v-model="username"
            placeholder="Username"
          />
          <input-component
            class="password"
            v-model="password"
            placeholder="Password"
            :hide="true"
          />
        </div>
        <icon-button-component class="add">
          <template #icon>
            <span class="add-icon">
              <img src="@/assets/images/add.svg" alt="Settings" />
            </span>
          </template>
          <template #text>
            <span class="add-text">add website</span>
          </template>
        </icon-button-component>
        <textarea-component
          class="notes"
          v-model="notes"
          placeholder="Write your notes here..."
        />
        <button-component class="save">Save</button-component>
      </div>
    </template>
  </pop-up-component>
</template>

<script>
import { mapState, mapMutations } from "vuex";

import PopUpComponent from "@/ui/components/PopUpComponent";
import CloseComponent from "@/ui/components/CloseComponent";
import InputComponent from "@/ui/components/InputComponent";
import IconButtonComponent from "@/ui/components/IconButtonComponent";
import ButtonComponent from "@/ui/components/ButtonComponent";
import TextareaComponent from "@/ui/components/TextareaComponent";

export default {
  components: {
    PopUpComponent,
    CloseComponent,
    InputComponent,
    ButtonComponent,
    IconButtonComponent,
    TextareaComponent,
  },
  data() {
    return {
      username: "",
      password: "",
      notes: "",
    };
  },
  computed: {
    ...mapState("home", ["popUpActive"]),
  },
  methods: {
    ...mapMutations("home", ["togglePopUp"]),
  },
};
</script>

<style lang="scss" scoped>
.pop-up > * {
  border-radius: calc($border-radius * 3);
  background: $light-main-color;
  padding: $gap;
  max-width: 500px;
  width: 100%;
}

.content {
  max-width: 270px;
  margin: 0 auto;
  padding: calc($gap * 2) $gap;
  display: flex;
  flex-direction: column;
  gap: $gap;
  align-items: center;
}

.close {
  width: 27px;
  height: 27px;
  margin-left: auto;
}

.username,
.password,
.add,
.notes {
  background: $dark-main-color;
  width: 100%;
}

.username > *,
.password > *,
.notes > * {
  color: $text-color;
  font-size: 15px;
  letter-spacing: 3px;
}

.username,
.password {
  height: $small-elem-height;
}

.password {
  border-radius: 0 0 $border-radius $border-radius;
  border-top: 2px solid $light-main-color;
}

.username {
  border-radius: $border-radius $border-radius 0 0;
}

.add {
  font-size: 15px;
  height: $small-elem-height;
  letter-spacing: 3.8px;
  font-weight: 400;
  color: $blue-color;
}

.add-icon {
  margin-top: 2px;
}

.add-text {
  margin-left: 12px;
}

.notes {
  font-size: 15px;
  height: 120px;
  padding-top: $small-gap;
  padding-top: $small-gap;
}

.save {
  background: $green-color;
  font-size: 15px;
  height: $small-elem-height;
  letter-spacing: 2.4px;
  text-indent: 2.4px;
  padding: 0 calc($gap / 2);
}
</style>
