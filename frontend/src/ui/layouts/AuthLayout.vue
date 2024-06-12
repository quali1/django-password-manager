<template>
  <div class="auth">
    <div class="inputs">
      <slot name="inputs"></slot>
    </div>
    <div class="buttons">
      <slot name="buttons"></slot>
    </div>
    <div class="text">
      <div class="errors">
        <slot name="errors"></slot>
      </div>
      <div class="links">
        <slot name="links"></slot>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.auth {
  height: 100%;
  display: flex;
  gap: 36px;
  padding: $gap;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.inputs {
  display: flex;
  gap: 36px;
  flex-direction: column;
  max-width: 360px;
  width: 100%;

  & > * {
    background: $dark-main-color;
  }

  & > * > * {
    color: $dark-text-color;
    font-size: 20px;
    letter-spacing: 3.6px;
    transition: color $transition;
  }
}

.buttons > * {
  width: 180px;
  background: $blue-color;
  font-size: 20px;
  height: $elem-height;
  letter-spacing: 5px;
  text-indent: 5px;
  text-transform: uppercase;
}

.text {
  text-align: center;
  margin-top: -5px;
}

.links {
  margin-top: -2px;

  & > * {
    color: $dark-text-color;
    font-size: 14px;
    letter-spacing: 2.8px;
    line-height: 150%;
    transition: opacity $transition;

    &:hover {
      opacity: 0.8;
    }
  }
}
</style>
