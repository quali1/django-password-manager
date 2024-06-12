<template>
  <expandable-component class="error" :active="isError">
    <div class="container">{{ error }}</div>
  </expandable-component>
</template>

<script>
import { mapState, mapActions } from "vuex";

import ExpandableComponent from "@/ui/components/ExpandableComponent";

export default {
  components: {
    ExpandableComponent,
  },
  computed: {
    ...mapState("error", ["error", "isError"]),
  },
  methods: {
    ...mapActions("error", ["clearError"]),
  },
  mounted() {
    this.clearError();
  },
};
</script>

<style lang="scss" scoped>
.error {
  color: $red-color;
  font-size: 18px;
  letter-spacing: 3.6px;
}

.error:not(.active) {
  opacity: 0;
}

.container {
  min-height: calc($gap * 2 - 8px + 18px);
}
</style>
