//
//  __FileName__
//  __ProjectName__
//
//  Created by __UserName__ on __Date__.
//  Copyright (c) __Year__ __OrganizationName__. All rights reserved.
//


import Foundation

final class __ModuleName__Presenter {

    // MARK: - Private properties -

    private unowned let view: __ModuleName__ViewInterface
    private let interactor: __ModuleName__InteractorInterface
    private let wireframe: __ModuleName__WireframeInterface

    // MARK: - Lifecycle -

    init(view: __ModuleName__ViewInterface, interactor: __ModuleName__InteractorInterface, wireframe: __ModuleName__WireframeInterface) {
        self.view = view
        self.interactor = interactor
        self.wireframe = wireframe
    }
}

// MARK: - Extensions -

extension __ModuleName__Presenter: __ModuleName__PresenterInterface {
}
