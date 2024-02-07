Feature: Verificación de las secciones "HOME" y "WHO WE ARE" en el sitio web BCNC

Scenario: Verificar la sección "HOME"
    Given que estoy en la página de inicio
    When hago clic en el enlace "HOME"
    Then debería ver los párrafos en la sección "HOME"

Scenario: Verificar la sección "WHO WE ARE"
    Given que estoy en la página de inicio
    When hago clic en el enlace "WHO WE ARE"
    Then debería ver los párrafos en la sección "WHO WE ARE"