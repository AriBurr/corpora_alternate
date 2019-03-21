import styled from "vue-styled-components";
// import ReadStyleGuide from "../../styles/ReadStyleGuide";
import { themeProps } from "./ThemeProps";

export const StyledDiv = styled("div", themeProps)`
  align-items: ${props => props.alignItems || "center"};
  align-self: ${props => props.alignSelf || null};
  background-color: ${props => props.backgroundColor || null};
  background: ${props => props.background};
  background-image: url(${props => props.backgroundImage || null});
  background-repeat: ${props => props.backgroundRepeat || "no-repeat"};
  background-attachment: ${props => props.backgroundAttachment || null};
  background-position: ${props => props.backgroundPosition || "center center"};
  background-size: ${props => props.backgroundSize || null};
  border: ${props => props.border};
  border-top: ${props => props.borderTop || null};
  border-bottom: ${props => props.borderBottom || null};
  border-right: ${props => props.borderRight || null};
  border-left: ${props => props.borderLeft || null};
  border-radius: ${props => props.borderRadius || null};
  bottom: ${props => props.bottom};
  box-shadow: ${props => props.boxShadow || null};
  display: ${props => props.display || "flex"};
  flex: ${props => props.flex};
  flex-direction: ${props => props.flexDirection || "column"};
  flex-wrap: ${props => props.flexWrap || null};
  height: ${props => props.height || "100%"};
  justify-content: ${props => props.justifyContent || "center"};
  left: ${props => props.left};
  margin: ${props => props.margin};
  max-height: ${props => props.maxHeight || null};
  max-width: ${props => props.maxWidth || null};
  min-height: ${props => props.minHeight || null};
  opacity: ${props => props.opacity || null};
  order: ${props => props.order};
  overflow: ${props => props.overflow};
  position: ${props => props.position};
  padding: ${props => props.padding};
  right: ${props => props.right};
  top: ${props => props.top};
  width: ${props => props.width || "100%"};
  z-index: ${props => props.zIndex || null};

  &:hover {
    transform: ${props => props.transformation || null};
    background: ${props => props.hoverBackgroundColor};
    filter: ${props => props.hoverBrightness || null};
    background-size: ${props => props.hoverBackgroundSize};
    cursor: ${props => props.cursor};
    border-radius: ${props => props.hoverBorderRadius};
    color: ${props => props.hoverColor};
  }
`;
