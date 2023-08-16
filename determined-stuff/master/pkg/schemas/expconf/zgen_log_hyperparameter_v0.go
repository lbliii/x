// Code generated by gen.py. DO NOT EDIT.

package expconf

import (
	"github.com/santhosh-tekuri/jsonschema/v2"

	"github.com/determined-ai/determined/master/pkg/schemas"
)

func (l LogHyperparameterV0) Minval() float64 {
	return l.RawMinval
}

func (l *LogHyperparameterV0) SetMinval(val float64) {
	l.RawMinval = val
}

func (l LogHyperparameterV0) Maxval() float64 {
	return l.RawMaxval
}

func (l *LogHyperparameterV0) SetMaxval(val float64) {
	l.RawMaxval = val
}

func (l LogHyperparameterV0) Base() float64 {
	return l.RawBase
}

func (l *LogHyperparameterV0) SetBase(val float64) {
	l.RawBase = val
}

func (l LogHyperparameterV0) Count() *int {
	return l.RawCount
}

func (l *LogHyperparameterV0) SetCount(val *int) {
	l.RawCount = val
}

func (l LogHyperparameterV0) ParsedSchema() interface{} {
	return schemas.ParsedLogHyperparameterV0()
}

func (l LogHyperparameterV0) SanityValidator() *jsonschema.Schema {
	return schemas.GetSanityValidator("http://determined.ai/schemas/expconf/v0/hyperparameter-log.json")
}

func (l LogHyperparameterV0) CompletenessValidator() *jsonschema.Schema {
	return schemas.GetCompletenessValidator("http://determined.ai/schemas/expconf/v0/hyperparameter-log.json")
}
