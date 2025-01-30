		# Discrete Mathematics: Logical Operations

		## Logical Operators

		### Conjunction (AND) $$p \land q$$

		- Symbol: $$\land$$ (LaTeX), $$^$$ (ASCII)
		- Truth table:

		| $$p$$ | $$q$$ | $$p \land q$$ |

		|-------|-------|--------------|

		| T | T | T |

		| T | F | F |

		| F | T | F |

		| F | F | F |

		### Disjunction (OR) $$p \lor q$$

		- Symbol: $$\lor$$ (LaTeX), $$\vee$$ (ASCII)
		- Truth table:

		| $$p$$ | $$q$$ | $$p \lor q$$ |

		|-------|-------|--------------|

		| T | T | T |

		| T | F | T |

		| F | T | T |

		| F | F | F |

		## De Morgan's Laws

		1. Negation of Conjunction:

		$$\neg(p \land q) \equiv \neg p \lor \neg q$$

		2. Negation of Disjunction:

		$$\neg(p \lor q) \equiv \neg p \land \neg q$$

		## Propositional Equivalences

		### Law of Excluded Middle

		$$p \lor \neg p = \text{true}$$

		### Commutative Property

		- $$p \land q \equiv q \land p$$
		- $$p \lor q \equiv q \lor p$$

		### Associative Property

		- $$\big(p \land q\big) \land r \equiv p \land \big(q \land r\big)$$
		- $$\big(p \lor q\big) \lor r \equiv p \lor \big(q \lor r\big)$$

		## Python Implementation Example

		```python
		def and_operation(p, q):
		    """Implement logical AND operation"""
		    return p and q
		def or_operation(p, q):
		    """Implement logical OR operation"""
		    return p or q
		def de_morgans_law_1(p, q):
		    """Demonstrate first De Morgan's Law"""
		    return not(p and q) == (not p or not q)
		def de_morgans_law_2(p, q):
		    """Demonstrate second De Morgan's Law"""
		    return not(p or q) == (not p and not q)
		```

		## Key Takeaways

		- Logical operations form the foundation of Boolean algebra
		- De Morgan's Laws provide rules for negating compound propositions
		- Understanding these principles is crucial in computer science, especially in logic design and programming