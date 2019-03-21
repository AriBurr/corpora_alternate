import styled from "vue-styled-components";
import ReadStyleGuide from "../../styles/ReadStyleGuide";
import { themeProps } from "./ThemeProps";

export const StyledButton = styled("button", themeProps)`
  border: ${props => props.border || "none"};
  background-color: ${props =>
    props.backgroundColor || ReadStyleGuide.color.lightBlue};
  border-radius: ${props => props.borderRadius || "15px"};
  color: ${props => props.color || ReadStyleGuide.color.white};
  font-size: ${props => props.fontSize || ReadStyleGuide.font.size.medium};
  font-weight: ${props => props.fontWeight};
  padding: ${props => props.padding || "0 20px"};
  width: ${props => props.width || "initial"};

  &:hover {
    cursor: ${props => props.cursor || "pointer"};
    box-shadow: ${props => props.boxShadow};
    filter: ${props => props.hoverBrightness};
    transform: ${props => props.hoverScale};
  }
`;
