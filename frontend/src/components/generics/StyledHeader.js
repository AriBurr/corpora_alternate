import styled from "vue-styled-components";
import { themeProps } from "./ThemeProps";
import ReadStyleGuide from "../../styles/ReadStyleGuide";
import { media } from "./MediaSizes";

export const StyledHeader = styled("h1", themeProps)`
  width: ${props => props.width || "initial"};
  text-align: ${props => props.textAlign || "center"};
  color: ${props => props.color || ReadStyleGuide.color.darkBlue};
  font-family: ${props => props.fontFamily || ReadStyleGuide.font.family.chivo};
  font-size: ${props => props.fontSize || ReadStyleGuide.font.size.large};
  white-space: ${props => props.whiteSpace || "pre-line"};
  ${props => (props.margin ? `margin: ${props.margin}` : null)};
  ${props => (props.padding ? `padding: ${props.padding}` : null)};
  ${props => (props.fontWeight ? `font-weight: ${props.fontWeight}` : null)};
  ${props => (props.fontStyle ? `font-style: ${props.fontStyle}` : null)};

  &:hover {
    color: ${props => props.hoverColor || null};
    cursor: ${props => props.cursorType || null};
  }

  ${media.desktop`${props =>
    props.desktopFontSize ? `font-size:${props.desktopFontSize}` : null}`};
  ${media.tablet`${props =>
    props.tabletSize ? `font-size: ${props.tabletSize}` : null}`};
  ${media.phone`font-size: ${props => props.phoneFontSize || null};`};
`;
