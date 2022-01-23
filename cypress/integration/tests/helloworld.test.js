/// <reference types="cypress" />

describe('Hello world tests!', () => {

  it('Visit localhost', () => {
    cy.visit(`http://localhost:8010`)
  })

  it('Click on "BLOG" button', () => {
    cy.get('#blog-button-link').click()
  })

})
