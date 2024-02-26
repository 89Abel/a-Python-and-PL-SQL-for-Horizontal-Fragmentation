CREATE OR REPLACE TYPE miniterm_type AS OBJECT (
    relation VARCHAR2(100),
    predicate VARCHAR2(200)
);
/

CREATE OR REPLACE TYPE miniterm_list AS TABLE OF miniterm_type;
/

CREATE OR REPLACE FUNCTION generate_fragments(relations miniterm_list, predicates miniterm_list) RETURN miniterm_list
IS
    fragments miniterm_list := miniterm_list();
BEGIN
    FOR i IN 1..predicates.COUNT LOOP
        FOR j IN 1..relations.COUNT LOOP
            fragments.EXTEND;
            fragments(fragments.LAST) := miniterm_type(relations(j).relation, predicates(i).predicate);
        END LOOP;
    END LOOP;
    RETURN fragments;
END;
/
