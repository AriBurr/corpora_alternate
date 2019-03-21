import styled from "vue-styled-components";
import { themeProps } from "./ThemeProps";
import ReadStyleGuide from "../../styles/ReadStyleGuide";
import { media } from "./MediaSizes";

export const StyledParagraph = styled("p", themeProps)`
  color: ${props => props.color || ReadStyleGuide.color.darkBlue};
  font-style: ${props => props.fontStyle || "initial"};
  font-family: ${props => props.fontFamily || ReadStyleGuide.font.family.chivo};
  font-size: ${props => props.fontSize || ReadStyleGuide.font.size.small};
  line-height: ${props => props.fontHeight || "1"};
  text-align: ${props => props.textAlign || "left"};
  white-space: ${props => props.whiteSpace || "pre-line"};
  ${props => (props.border ? `border:${props.border}` : null)};
  ${props => (props.width ? `width:${props.width}` : null)};
  ${props => (props.margin ? `margin:${props.margin}` : null)};
  ${props =>
    props.textDecoration ? `text-decoration: ${props.textDecoration}` : null};
  ${props => (props.padding ? `padding: ${props.padding}` : null)};
  ${props => (props.fontWeight ? `font-weight:${props.fontWeight}` : null)};
  ${props => (props.textAlign ? `text-align:${props.textAlign}` : null)};

  &:hover {
    color: ${props => props.hoverColor || null};
    cursor: ${props => props.cursorType || null};
}

  ${media.desktop`
    font-size: ${props => props.tabletFontSize}; 
    text-align: ${props => props.deskotpTextAlign}
  `}
  ${media.tablet`
    font-size: ${props => props.smallTabletFontSize};
  `}
  ${media.phone`
    font-size: ${props => props.mobileFontSize};
  `}
`;
