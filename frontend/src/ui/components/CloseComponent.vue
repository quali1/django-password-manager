<template>
  <div class="close">
    <img class="circle" src="@/assets/images/close-circle.svg" alt="Circle" />
    <img class="cross" src="@/assets/images/close.svg" alt="Close" />
  </div>
</template>

<style lang="scss" scoped>
.close {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity $transition;
  cursor: pointer;

  &:hover {
    opacity: $hover-opacity;
  }
}

.circle {
  position: absolute;
  width: 100%;
  height: 100%;
  animation: rotate-animation 7s infinite linear;
}

.cross {
  width: 33%;
  height: 33%;
}

.close:hover .circle {
  animation-play-state: paused;
}

@keyframes rotate-animation {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
