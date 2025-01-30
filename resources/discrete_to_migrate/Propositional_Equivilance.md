			Propositional Equivilance

	## 1. Distributive Law

	### Theorem

	$$p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$$

	### Truth Table Proof

	| $p$ | $q$ | $r$ | $p \land (q \lor r)$ | $(p \land q) \lor (p \land r)$ | Equivalent |

	|-----|-----|-----|---------------------|-------------------------------|------------|

	| T | T | T | T | T | ✓ |

	| T | T | F | T | T | ✓ |

	| T | F | T | T | T | ✓ |

	| T | F | F | F | F | ✓ |

	| F | T | T | F | F | ✓ |

	| F | T | F | F | F | ✓ |

	| F | F | T | F | F | ✓ |

	| F | F | F | F | F | ✓ |

	**Conclusion**: The truth table demonstrates logical equivalence.

	## 2. De Morgan's Laws

	### Law 1: Negation of Conjunction

	$$\lnot(p \land q) \equiv (\lnot p) \lor (\lnot q)$$

	### Truth Table

	| $p$ | $q$ | $\lnot(p \land q)$ | $(\lnot p) \lor (\lnot q)$ | Equivalent |

	|-----|-----|-------------------|----------------------------|------------|

	| T | T | F | F | ✓ |

	| T | F | T | T | ✓ |

	| F | T | T | T | ✓ |

	| F | F | T | T | ✓ |

	### Law 2: Negation of Disjunction

	$$\lnot(p \lor q) \equiv (\lnot p) \land (\lnot q)$$

	### Truth Table

	| $p$ | $q$ | $\lnot(p \lor q)$ | $(\lnot p) \land (\lnot q)$ | Equivalent |

	|-----|-----|-------------------|----------------------------|------------|

	| T | T | F | F | ✓ |

	| T | F | F | F | ✓ |

	| F | T | F | F | ✓ |

	| F | F | T | T | ✓ |

	## 3. Associative Property

	### Conjunction

	$$p \land (q \land r) \equiv (p \land q) \land r$$

	### Truth Table

	| $p$ | $q$ | $r$ | $p \land (q \land r)$ | $(p \land q) \land r$ | Equivalent |

	|-----|-----|-----|----------------------|----------------------|------------|

	| T | T | T | T | T | ✓ |

	| T | T | F | F | F | ✓ |

	| T | F | T | F | F | ✓ |

	| F | T | T | F | F | ✓ |

	| F | F | T | F | F | ✓ |

	| F | T | F | F | F | ✓ |

	| T | F | F | F | F | ✓ |

	| F | F | F | F | F | ✓ |

	### Disjunction

	$$p \lor (q \lor r) \equiv (p \lor q) \lor r$$

	(Truth table follows similar pattern and demonstrates equivalence)

	## 4. Commutative Property

	### Conjunction

	$$p \land q \equiv q \land p$$

	### Disjunction

	$$p \lor q \equiv q \lor p$$

	### Truth Tables Demonstrate Equivalence

	(Omitted for brevity, follows identical pattern of symmetric truth values)

	## 5. Absorption Law

	### Theorem

	$$p \lor (p \land q) \equiv p$$

	### Truth Table

	| $p$ | $q$ | $p \lor (p \land q)$ | $p$ | Equivalent |

	|-----|-----|---------------------|-----|------------|

	| T | T | T | T | ✓ |

	| T | F | T | T | ✓ |

	| F | T | F | F | ✓ |

	| F | F | F | F | ✓ |

	## Conclusion

	These proofs systematically demonstrate the fundamental logical equivalences through truth table analysis, showing how logical propositions can be transformed and simplified while maintaining their essential truth conditions.