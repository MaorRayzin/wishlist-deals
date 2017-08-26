import {PENDING, FULFILLED, REJECTED} from 'redux-promise-middleware';

function getTypeWithSuffix(actionType, actionStatus) {
    return actionType + '_' + actionStatus;
}

export function getPendingType(actionType) {
    return getTypeWithSuffix(actionType, PENDING);
}

export function getFulfilledType(actionType) {
    return getTypeWithSuffix(actionType, FULFILLED);
}

export function getRejectedType(actionType) {
    return getTypeWithSuffix(actionType, REJECTED);
}
