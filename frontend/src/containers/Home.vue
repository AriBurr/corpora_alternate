<template>
  <StyledDiv class="home" height="418px">
    <StyledHeader margin="0 5px" class="read-header">READ Toolkit</StyledHeader>
    <StyledButton>hello</StyledButton>
  </StyledDiv>
</template>

<script>
import { StyledButton } from "../components/generics/StyledButton.js";
import { StyledDiv } from "../components/generics/StyledDiv.js";
import { StyledHeader } from "../components/generics/StyledHeader.js";

export default {
  name: "home",
  components: { StyledButton, StyledDiv, StyledHeader }
};
</script>

<style>
.home {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
