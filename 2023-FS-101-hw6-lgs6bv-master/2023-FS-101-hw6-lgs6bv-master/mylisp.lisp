;; myLast
(defun myLast (L)
  (cond
    ((null (cdr L)) (car L))
    (t (myLast (cdr L)))))

;; myCount
(defun myCount (X L)
  (cond
    ((null L) 0)
    ((eql X (car L)) (+ 1 (myCount X (cdr L))))
    (t (myCount X (cdr L)))))

;; myMember
(defun myMember (X L)
  (cond
    ((null L) nil)
    ((eql X (car L)) t)
    (t (myMember X (cdr L)))))

;; myPurge
(defun myPurge (L)
  (cond
    ((null L) nil)
    ((myMember (car L) (cdr L)) (myPurge (cdr L)))
    (t (cons (car L) (myPurge (cdr L))))))

;; myCommon
(defun myCommon (L1 L2)
  (cond
    ((null L1) nil)
    ((myMember (car L1) L2) (cons (car L1) (myCommon (cdr L1) L2)))
    (t (myCommon (cdr L1) L2))))

;; myGen
(defun myGen (X Y)
  (cond
    ((> X Y) nil)
    (t (cons X (myGen (+ X 1) Y)))))

;; myMap
(defun myMap (F L)
  (cond
    ((null L) nil)
    (t (cons (funcall F (car L)) (myMap F (cdr L))))))

;; myReduce
(defun myReduce (F L)
  (cond
    ((null (cdr L)) (car L))
    (t (funcall F (car L) (myReduce F (cdr L))))))

;; Testing Examples
(format t "myLast: ~a~%" (myLast '(p a e g)))                  
(format t "myCount: ~a~%" (myCount 'a '(p k a t p a e g)))    ; Output: 2
(format t "myMember: ~a~%" (myMember 'a '(p a e g)))           ; Output: T
(format t "myPurge: ~a~%" (myPurge '(p a c e p c)))           ; Output: (a e p c)
(format t "myCommon: ~a~%" (myCommon '(p a e g) '(a q r e)))  ; Output: (a e)
(format t "myGen: ~a~%" (myGen 3 11))                          ; Output: (3 4 5 6 7 8 9 10 11)
(format t "myGen: ~a~%" (myGen 4 4))                           ; Output: (4)
(format t "myGen: ~a~%" (myGen 11 3))                          ; Output: ()
(format t "myMap: ~a~%" (myMap (lambda (x) (* 2 x)) '(1 2 3 4))) ; Output: (2 4 6 8)
(format t "myReduce: ~a~%" (myReduce (lambda (x y) (+ x y)) '(1 2 3 4 5))) ; Output: 15