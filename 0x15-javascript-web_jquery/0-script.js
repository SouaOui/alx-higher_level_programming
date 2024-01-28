#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function () {
  const headerElement = document.querySelector('header');

  if (headerElement) {
    headerElement.style.color = '#FF0000';
  } else {
    console.error('Header element not found.');
  }
});
