<template>
  <div class="add-profile">
    <add-form-layout>
      <template #inputs>
        <input-component
          class="input title"
          v-model="title"
          placeholder="Username"
          :error="!title && isError"
        />
        <expandable-button-component class="notes-button">
          <template #text>
            <span class="button-text">Pin</span>
          </template>
          <template #content>
            <input-component
              class="input pin"
              v-model="pin"
              :error="!pin && isError"
              :hide="true"
              :type="'number'"
            />
          </template>
        </expandable-button-component>
      </template>
      <template #buttons>
        <button-component class="button" @click="submit">Save</button-component>
      </template>
    </add-form-layout>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

import InputComponent from "@/ui/components/InputComponent";
import ButtonComponent from "@/ui/components/ButtonComponent";
import ExpandableButtonComponent from "@/ui/components/ExpandableButtonComponent";
import AddFormLayout from "@/ui/layouts/AddFormLayout";

export default {
  components: {
    InputComponent,
    ButtonComponent,
    ExpandableButtonComponent,
    AddFormLayout,
  },
  data() {
    return {
      title: "",
      pin: "",
    };
  },
  computed: {
    ...mapState("error", ["isError"]),
  },
  methods: {
    ...mapActions("profiles", ["addProfiles"]),
    ...mapActions("error", ["setError"]),
    submit() {
      if (!this.title) {
        this.setError("Fill in all the fields!");
      } else {
        this.addProfiles({
          title: this.title,
          pin: this.pin,
        });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.input {
  background: $dark-main-color;
  width: 100%;

  & > * {
    color: $dark-text-color;
    font-size: 20px;
    letter-spacing: 3.6px;
    transition: color $transition;
  }
}

.pin {
  margin-top: 0;
}

.notes-button > * {
  background: $dark-main-color;

  &:nth-child(1) {
    height: $elem-height;
  }

  &:nth-child(2) > * {
    padding: 0;
  }
}

.button-text {
  color: $dark-text-color;
  letter-spacing: 3.6px;
  opacity: $placeholder-opacity;
  font-size: 20px;
}

.button-img {
  width: 20px;
  display: flex;
  justify-content: center;
}
</style>
