<template>
  <div class="add-password">
    <div class="header">
      <back-component />
    </div>
    <div class="inputs">
      <input-component
        class="input username"
        v-model="username"
        placeholder="Username"
        :error="!username && isError"
      />
      <input-component
        class="input password"
        v-model="password"
        placeholder="Password"
        :error="!password && isError"
        :hide="true"
      />
      <input-component
        class="input website"
        v-model="website"
        :error="!website && isError"
        placeholder="Website"
      />
      <expandable-button-component class="notes-button">
        <template #text>
          <span class="button-text">Notes</span>
        </template>
        <template #content>
          <textarea-component
            class="textarea notes"
            v-model="notes"
            placeholder="Write your notes here..."
          />
        </template>
      </expandable-button-component>
    </div>
    <div class="buttons">
      <button-component class="button" @click="submit">Save</button-component>
    </div>
    <div class="errors">
      <error-component />
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

import InputComponent from "@/ui/components/InputComponent";
import ButtonComponent from "@/ui/components/ButtonComponent";
import TextareaComponent from "@/ui/components/TextareaComponent";
import ExpandableButtonComponent from "@/ui/components/ExpandableButtonComponent";
import ErrorComponent from "@/ui/components/ErrorComponent";
import BackComponent from "@/ui/components/BackComponent";

export default {
  components: {
    InputComponent,
    ButtonComponent,
    TextareaComponent,
    ExpandableButtonComponent,
    ErrorComponent,
    BackComponent,
  },
  data() {
    return {
      username: "",
      password: "",
      website: "",
      notes: "",
    };
  },
  computed: {
    ...mapState("error", ["isError"]),
  },
  methods: {
    ...mapActions("passwords", ["addPassword"]),
    ...mapActions("error", ["setError"]),
    submit() {
      if (!(this.website && this.username && this.password)) {
        this.setError("Fill in all the fields!");
      } else {
        this.addPassword({
          username: this.username,
          password: this.password,
          website: this.website,
          notes: this.notes,
        });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.add-password {
  display: flex;
  flex-direction: column;
  gap: 36px;
}

.header {
  width: 100%;
  max-width: 360px;
}

.inputs {
  display: flex;
  flex-direction: column;
  max-width: 360px;
  gap: 36px;
}

.input,
.textarea {
  background: $dark-main-color;
  width: 100%;

  & > * {
    color: $dark-text-color;
    font-size: 20px;
    letter-spacing: 3.6px;
    transition: color $transition;
  }
}

.notes-button > * {
  background: $dark-main-color;

  &:nth-child(1) {
    height: $elem-height;
  }

  &:nth-child(2) > * {
    padding: $small-gap 0;
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

.button {
  width: 180px;
  background: $blue-color;
  font-size: 20px;
  height: $elem-height;
  letter-spacing: 5px;
  text-transform: uppercase;
}

.textarea {
  height: 150px;
}

.errors {
  margin: 0;
}
</style>
