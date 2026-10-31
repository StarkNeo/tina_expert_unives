(deftemplate tina
   (slot nivel-anterior)
   (slot nivel-actual))

(deftemplate estado
   (slot valor))

(deftemplate recomendacion
   (slot accion))

;; TINA VACÍA
(defrule tina-vacia
   (tina (nivel-actual 0)) => (assert (estado (valor vacia)))
   (assert (recomendacion (accion "Abrir válvula de llenado")))
)


;; TINA LLENA
(defrule tina-llena
   (tina (nivel-actual 100)) => (assert (estado (valor llena)))
   (assert (recomendacion (accion "Cerrar entrada de agua")))
)




;; LLENÁNDOSE
(defrule tina-llenandose
   (tina (nivel-anterior ?a) (nivel-actual ?b))
   (test (> ?b ?a))
   (test (< ?b 100))
   =>
   (assert (estado (valor llenandose)))
   (assert (recomendacion (accion "Continuar monitoreo")))
)

;; VACIÁNDOSE

(defrule tina-vaciandose
   (tina (nivel-anterior ?a) (nivel-actual ?b))
   (test (< ?b ?a))
   (test (> ?b 0))
   =>
   (assert (estado (valor vaciandose)))
   (assert (recomendacion (accion "Verificar drenaje")))
   
)
   


;; ESTABLE

(defrule tina-estable

   (tina (nivel-anterior ?a) (nivel-actual ?a))
   (test (> ?a 0))
   (test(< ?a 100))
   =>
   (assert (estado (valor estable)))
   (assert (recomendacion (accion "Mantener operación actual")))
)