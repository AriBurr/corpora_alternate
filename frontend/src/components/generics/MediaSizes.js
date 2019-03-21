import { css } from "vue-styled-components";

const sizes = {
  cardsToSmall: 1210,
  giant: 1170,
  desktop: 1100,
  oneThousand: 1000,
  nineHundred: 900,
  eightHundred: 800,
  tablet: 768,
  phone: 400
};

export const media = Object.keys(sizes).reduce((accumulator, label) => {
  // use em in breakpoints to work properly cross-browser and support users
  // changing their browsers font-size: https://zellwk.com/blog/media-query-units/
  const emSize = sizes[label] / 16;
  accumulator[label] = (...args) =>
    css`
      @media (max-width: ${emSize}em) {
        ${css(...args)};
      }
    `;
  return accumulator;
}, {});
